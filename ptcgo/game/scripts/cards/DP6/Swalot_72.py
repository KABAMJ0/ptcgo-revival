from ptcgo.game.card_effects.attacks_common import bonus_if, condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack


def _defender_below_own_hp(ctx) -> bool:
    defender, attacker = ctx.defender, ctx.attacker
    return (defender is not None and attacker is not None
            and defender.get_attribute(AttrID.HP, 0)
            < attacker.get_attribute(AttrID.HP, 0))

card = PokemonCardDef(
    guid="8652a85b-ca6c-5628-baca-1f7cf47f0f13",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swalot.Name",
    display_name="Swalot",
    searchable_by=["Swalot", "Stage 1", "Swalot"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gulpin.Name",
    family_id=316,
    abilities=[
        Attack(
            title="Swallow Up",
            game_text="Before doing damage, count the remaining HP of the Defending Pok\u00e9mon and Swalot. If the Defending Pok\u00e9mon has fewer remaining HP than Swalot's, this attack does 80 damage instead.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=bonus_if(_defender_below_own_hp, 50, base=30),
        ),
        Attack(
            title="Gunk Shot",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)