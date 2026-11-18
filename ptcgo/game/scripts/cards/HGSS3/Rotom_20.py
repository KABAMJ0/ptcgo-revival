from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca7c6cb6-3645-52fa-b12b-93053aac4cee",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="HGSS3",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=479,
    abilities=[
        Ability(
            title="Mischievous Trick",
            game_text="Once during your turn (before your attack), you may switch 1 of your face-down Prize cards with the top card of your deck. This power can't be used if Rotom is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Plasma Arrow",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage for each Energy attached to that Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
    ],
)