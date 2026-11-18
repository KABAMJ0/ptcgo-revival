from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="313c2ffd-ca6d-518e-bc02-7677d749e7d8",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SuicuneEnteiLEGEND.Name",
    display_name="Suicune & Entei LEGEND",
    searchable_by=["Suicune & Entei LEGEND", "LEGEND", "SuicuneEnteiLEGEND"],
    subtypes=["LEGEND"],
    collector_number=94,
    set_code="HGSS2",
    rarity=Rarities.Common,
    hp=160,
    elements=[PokemonTypes.WATER, PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=244,
    abilities=[
        Attack(
            title="Torrent Blade",
            game_text="Return 2 Water Energy attached to Suicune & Entei LEGEND to your hand. Choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 100 damage to that Pok\u00e9mon. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Bursting Inferno",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)