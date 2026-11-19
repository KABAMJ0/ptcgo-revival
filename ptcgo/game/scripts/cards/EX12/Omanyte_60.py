from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import no_resistance_passive
from ptcgo.game.data_utils import def_for

_FOSSIL_ATTACKERS = ("omanyte", "omastar", "kabuto", "kabutops", "kabutops ex")


def _named(pokemon) -> str:
    definition = def_for(getattr(pokemon, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").strip().lower()


def _ancient_tentacles(calc, carrier) -> bool:
    attacker = calc.attacker
    return (calc.is_attack and attacker is not None
            and attacker.owning_player_id == carrier.owning_player_id
            and _named(attacker) in _FOSSIL_ATTACKERS)


card = PokemonCardDef(
    guid="97da7b83-28a3-5cae-947c-4f6498e2cd8c",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    display_name="Omanyte",
    searchable_by=["Omanyte", "Stage 1", "Omanyte"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="EX12",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=138,
    abilities=[
        Ability(
            title="Ancient Tentacles",
            game_text="Damage done to your opponent's Pok\u00e9mon by your Omanyte, Omastar, Kabuto, Kabutops, or Kabutops ex isn't affected by Resistance.",
            passive=no_resistance_passive(when=_ancient_tentacles),
        ),
        Attack(
            title="Rising Lunge",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(40)),
        ),
    ],
)