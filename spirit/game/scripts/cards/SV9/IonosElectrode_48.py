from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="92cdf8e2-2595-5e90-a214-832584b599a6",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosElectrode.Name",
    display_name="Iono's Electrode",
    searchable_by=["Iono's Electrode", "Stage 1", "IonosElectrode"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.IonosVoltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Thump-Thump Boom",
            game_text="This Pok\u00e9mon does 100 damage to itself. Flip a coin. If heads, your opponent's Active Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.LIGHTNING: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Electric Ball",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)