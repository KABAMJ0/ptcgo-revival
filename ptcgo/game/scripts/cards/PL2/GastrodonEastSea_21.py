from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1e7c5487-dfd9-56cf-b376-b501f4d56c4e",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GastrodonEastSea.Name",
    display_name="Gastrodon East Sea",
    searchable_by=["Gastrodon East Sea", "Stage 1", "GastrodonEastSea"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ShellosEastSea.Name",
    family_id=422,
    abilities=[
        Ability(
            title="Sticky Hold",
            game_text="If Gastrodon East Sea is switched or retreats to your Bench, move as many Energy cards attached to Gastrodon East Sea as you like to the new Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Calling Wave",
            game_text="Search your deck for up to 2 Gastrodon and put them onto your Bench as Basic Pok\u00e9mon. Put 2 damage counters on each of them. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)