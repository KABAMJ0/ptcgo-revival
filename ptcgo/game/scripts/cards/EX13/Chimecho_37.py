from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9ac51504-43b6-5e0b-b2ec-cd10c6950e8c",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimecho.Name",
    display_name="Chimecho δ",
    searchable_by=["Chimecho \u03b4", "Basic", "Chimecho"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=358,
    abilities=[
        Ability(
            title="Delta Support",
            game_text="Once during your turn (before your attack), if you have a Supporter card with Holon in its name in play, you may search your discard pile for a basic Energy card or a \u03b4 Rainbow Energy card, show it to your opponent, and put it into your hand. This power can't be used if Chimecho is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Hook",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)