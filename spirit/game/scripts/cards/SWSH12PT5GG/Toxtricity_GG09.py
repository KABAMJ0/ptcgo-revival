from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c29b6903-44bf-5577-8fb6-2ba3e6a64cce",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name",
    display_name="Toxtricity",
    searchable_by=["Toxtricity", "Stage 1", "Fusion Strike", "Toxtricity"],
    subtypes=["Stage 1", "Fusion Strike"],
    collector_number=9,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=849,
    abilities=[
        Ability(
            title="Maximum Downer",
            game_text="If all your Pok\u00e9mon in play are Fusion Strike Pok\u00e9mon, your opponent's Pok\u00e9mon VMAX in play get -30 HP.",
            effect=unimplemented,
        ),
        Attack(
            title="Head Bolt",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)