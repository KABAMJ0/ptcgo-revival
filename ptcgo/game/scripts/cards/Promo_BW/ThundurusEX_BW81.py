from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.pokemon import has_pokemon_subtype
from ptcgo.game.data_utils import def_for


def _benched_team_plasma(pokemon) -> bool:
    return not is_in_active_spot(pokemon) and \
        has_pokemon_subtype(pokemon, "Team Plasma")


def _plasma_energy_attached(ctx) -> bool:
    return any((getattr(def_for(energy.archetype_id), "display_name", "") or "")
               == "Plasma Energy" for energy in ctx.attached_energies(ctx.attacker))


async def _thunderous_noise(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if not _plasma_energy_attached(ctx):
        return
    if defender is not None and not ctx.effects_blocked(defender):
        await ctx.discard_energy_from(defender, 1)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="da2c2d06-00fe-5ae8-a5e7-335f93c3d623",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ThundurusEX.Name",
    display_name="Thundurus-EX",
    searchable_by=["Thundurus-EX", "Basic", "EX", "Team Plasma", "ThundurusEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=81,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=642,
    abilities=[
        Attack(
            title="Raiden Knuckle",
            game_text="Attach an Energy card from your discard pile to 1 of your Benched Team Plasma Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=attach_from_discard(count=1, target=_benched_team_plasma),
        ),
        Attack(
            title="Thunderous Noise",
            game_text="If this Pok\u00e9mon has any Plasma Energy attached to it, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=_thunderous_noise,
        ),
    ],
)