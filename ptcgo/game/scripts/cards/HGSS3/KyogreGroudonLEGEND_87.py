from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="130c0699-441c-56c1-8e4a-f9ff321fea6d",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyogreGroudonLEGEND.Name",
    display_name="Kyogre & Groudon LEGEND",
    searchable_by=["Kyogre & Groudon LEGEND", "LEGEND", "KyogreGroudonLEGEND"],
    subtypes=["LEGEND"],
    collector_number=87,
    set_code="HGSS3",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.WATER, PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Mega Tidal Wave",
            game_text="Discard the top 5 cards from your opponent's deck. This attack does 30 damage times the number of Energy cards you discarded to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Massive Eruption",
            game_text="Discard the top 5 cards from your deck. This attack does 100 damage times the number of Energy cards you discarded.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)