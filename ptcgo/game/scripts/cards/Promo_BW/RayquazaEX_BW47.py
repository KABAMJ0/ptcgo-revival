from ptcgo.game.card_effects.attacks_common import mill_then_attach_energy
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import mill_then_attach_energy

async def _dragon_burst(ctx):
    """Discard every basic Fire Energy or every basic Lightning Energy on this
    Pokemon (the player picks the type), 60 damage per card discarded."""
    attacker = ctx.attacker
    if attacker is None:
        return
    fire = [e for e in ctx.attached_energies(attacker)
            if basic_energy_of("fire")(e)]
    lightning = [e for e in ctx.attached_energies(attacker)
                 if basic_energy_of("lightning")(e)]
    pools = [pool for pool in (fire, lightning) if pool]
    if not pools:
        return
    pool = pools[0] if len(pools) == 1 else await ctx.choose_cards(
        [fire[0], lightning[0]], 1, prompt="Discard all Fire Energy or all Lightning Energy")
    if not pool:
        return
    if fire and pool[0] in fire:
        chosen = fire
    else:
        chosen = lightning
    await ctx.discard_cards(chosen)
    await ctx.deal_damage(60 * len(chosen))


card = PokemonCardDef(
    guid="378c0062-a37f-5c08-a612-1b76191ed012",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name",
    display_name="Rayquaza-EX",
    searchable_by=["Rayquaza-EX", "Basic", "EX", "RayquazaEX"],
    subtypes=["Basic", "EX"],
    collector_number=47,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    family_id=384,
    abilities=[
        Attack(
            title="Celestial Roar",
            game_text="Discard the top 3 cards of your deck. If any of those cards are Energy cards, attach them to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mill_then_attach_energy(count=3),
        ),
        Attack(
            title="Dragon Burst",
            game_text="Discard all basic Fire Energy or all basic Lightning Energy attached to this Pok\u00e9mon. This attack does 60 damage times the number of Energy you discarded.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=60,
            damage_operator="x",
            effect=_dragon_burst,
        ),
    ],
)