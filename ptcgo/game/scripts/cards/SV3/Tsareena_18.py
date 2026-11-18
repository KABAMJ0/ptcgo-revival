from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1a9a9545-6b40-50d2-b4a2-2e57e8bbd90c",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tsareena.Name",
    display_name="Tsareena",
    searchable_by=["Tsareena", "Stage 2", "Tsareena"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name",
    family_id=761,
    abilities=[
        Attack(
            title="Queenly Heel",
            game_text="During your opponent's next turn, Pok\u00e9mon can't be played from your opponent's hand to evolve the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Spinning Kick",
            game_text="This Pok\u00e9mon also does 20 damage to itself.",
            cost={PokemonTypes.GRASS: 2},
            damage=160,
            effect=recoil_attack(20),
        ),
    ],
)