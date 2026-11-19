from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f3db9b90-358e-5f7e-a2be-d77f194a2445",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darmanitan.Name",
    display_name="Darmanitan",
    searchable_by=["Darmanitan", "Stage 1", "Darmanitan"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    family_id=554,
    abilities=[
        Attack(
            title="Rolling Tackle",
            cost={PokemonTypes.FIRE: 2},
            damage=60,
        ),
        Attack(
            title="Inferno Onrush",
            game_text="This Pok\u00e9mon also does 70 damage to itself.",
            cost={PokemonTypes.FIRE: 3},
            damage=210,
            effect=recoil_attack(70),
        ),
    ],
)