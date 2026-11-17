from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2eeb284e-6b27-533d-8ea1-b55e6ceeaef8",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsSandaconda.Name",
    display_name="Hop's Sandaconda",
    searchable_by=["Hop's Sandaconda", "Stage 1", "HopsSandaconda"],
    subtypes=["Stage 1"],
    collector_number=87,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HopsSilicobra.Name",
    family_id=843,
    abilities=[
        Attack(
            title="Rumble",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Break Ground",
            game_text="This attack also does 20 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=unimplemented,
        ),
    ],
)