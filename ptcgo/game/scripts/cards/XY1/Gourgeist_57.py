from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8a9449fd-5c18-56c6-9b33-40ec24371d04",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gourgeist.Name",
    display_name="Gourgeist",
    searchable_by=["Gourgeist", "Stage 1", "Gourgeist"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    family_id=710,
    abilities=[
        Attack(
            title="Eerie Voice",
            game_text="Put 2 damage counters each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Spirit Scream",
            game_text="Put damage counters on both Active Pok\u00e9mon until the remaining HP of each Pok\u00e9mon is 10.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=unimplemented,
        ),
    ],
)