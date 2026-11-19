from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.pokemon import has_pokemon_subtype
from ptcgo.game.card_effects.support_common import attach_from_discard


def _plasma_energy_attached(ctx) -> bool:
    return any((getattr(def_for(energy.archetype_id), "display_name", "") or "")
               == "Plasma Energy" for energy in ctx.attached_energies(ctx.attacker))


def _benched_team_plasma(pokemon) -> bool:
    return not is_in_active_spot(pokemon) and \
        has_pokemon_subtype(pokemon, "Team Plasma")


async def thunderous_noise(ctx):
    """90 damage; with Plasma Energy attached, one Energy comes off the
    Defending Pokemon too."""
    await ctx.deal_damage()
    defender = ctx.defender
    if _plasma_energy_attached(ctx) and defender is not None \
            and not ctx.effects_blocked(defender):
        await ctx.discard_energy_from(
            defender, 1,
            prompt="Choose an Energy to discard from the Defending Pok\u00e9mon")

card = PokemonCardDef(
    guid="bb81a3a3-2a8e-58ba-a211-068fbbfa1ee7",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ThundurusEX.Name",
    display_name="Thundurus-EX",
    searchable_by=["Thundurus-EX", "Basic", "EX", "Team Plasma", "ThundurusEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=110,
    set_code="BW9",
    rarity=Rarities.RareUltra,
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
            effect=thunderous_noise,
        ),
    ],
)