from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9dd4452a-256e-58b8-92d9-8c65f10179d0",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaSlowbroex.Name",
    display_name="Mega Slowbro ex",
    searchable_by=["Mega Slowbro ex", "Stage 1", "MEGA", "ex", "MegaSlowbroex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=31,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="Shellnado Spin",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if this Pok\u00e9mon is Knocked Out), place 12 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=180,
            effect=unimplemented,
        ),
    ],
)