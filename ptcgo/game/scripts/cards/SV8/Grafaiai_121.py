from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6b755cfa-8704-5d8b-9a52-009e1d01157c",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grafaiai.Name",
    display_name="Grafaiai",
    searchable_by=["Grafaiai", "Stage 1", "Grafaiai"],
    subtypes=["Stage 1"],
    collector_number=121,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name",
    family_id=944,
    abilities=[
        Attack(
            title="Mischievous Painting",
            game_text="Attach up to 3 Energy cards from your opponent's discard pile to their Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Energized Graffiti",
            game_text="This attack does 40 damage for each Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)