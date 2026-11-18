from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c88738e0-3bb9-55c7-b9a1-4e988a9d68a0",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Politoed.Name",
    display_name="Politoed",
    searchable_by=["Politoed", "Stage 2", "Politoed"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="HGSS2",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Ability(
            title="Leap Frog",
            game_text="Once during your turn (before your attack), you may choose a Water Pok\u00e9mon on your Bench and switch it with your Active Pok\u00e9mon. This power can't be used if Politoed is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Big Chorus",
            game_text="Flip a coin for each Water Pok\u00e9mon you have in play. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)