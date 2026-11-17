from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2ad14082-275b-5760-a6d0-f91f99cbe57a",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inteleon.Name",
    display_name="Inteleon",
    searchable_by=["Inteleon", "Stage 2", "Inteleon"],
    subtypes=["Stage 2"],
    collector_number=142,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drizzile.Name",
    family_id=816,
    abilities=[
        Attack(
            title="Bring Down",
            game_text="Choose a Pok\u00e9mon in play (yours or your opponent's) that has the least HP remaining, except for this Pok\u00e9mon, and it is Knocked Out.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Water Shot",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=110,
            effect=unimplemented,
        ),
    ],
)