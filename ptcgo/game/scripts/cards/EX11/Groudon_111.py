from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_prizes_taken, self_energy_discard_attack
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def _critical_collection(ctx):
    await ctx.deal_damage()
    limit = count_prizes_taken("opponent")(ctx)
    if limit <= 0:
        return
    energy = [card for card in ctx.discard_pile()
              if energy_provides_type(card, PokemonTypes.FIGHTING.value)]
    if not energy:
        return
    picks = await ctx.choose_cards(energy, limit, minimum=0,
                                   prompt="Choose up to that many Fighting Energy to attach")
    for card in picks:
        await ctx.attach_energy(card, ctx.source)


card = PokemonCardDef(
    guid="2c732efa-6de7-5a74-890c-d164244d2bfa",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon ★",
    searchable_by=["Groudon \u2605", "Basic", "Star", "Groudon"],
    subtypes=["Basic", "Star"],
    collector_number=111,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=383,
    abilities=[
        Attack(
            title="Critical Collection",
            game_text="Count the number of Prize cards your opponent has taken. Search your discard pile for up to that many Fighting Energy cards and attach them to Groudon Star.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=_critical_collection,
        ),
        Attack(
            title="Ground Slash",
            game_text="Discard a Fighting Energy card attached to Groudon Star.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=self_energy_discard_attack(1, energy_type=PokemonTypes.FIGHTING),
        ),
    ],
)