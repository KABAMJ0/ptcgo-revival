from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c21e83eb-e950-58b8-b890-6ef6993d58c5",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsCorvisquire.Name",
    display_name="Hop's Corvisquire",
    searchable_by=["Hop's Corvisquire", "Stage 1", "HopsCorvisquire"],
    subtypes=["Stage 1"],
    collector_number=134,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HopsRookidee.Name",
    family_id=821,
    abilities=[
        Attack(
            title="Speed Dive",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)