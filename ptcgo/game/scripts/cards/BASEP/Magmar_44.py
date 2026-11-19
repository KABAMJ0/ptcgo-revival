from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type


def _fire_energy(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)


async def burning_fire(ctx):
    """Discard any number of Fire Energy from your Pokemon in play, then 10 plus
    10 for each one discarded."""
    pool = [energy for pokemon in ctx.my_pokemon_in_play()
            for energy in ctx.attached_energies(pokemon) if _fire_energy(energy)]
    discarded = []
    if pool:
        discarded = await ctx.choose_cards(
            pool, len(pool), minimum=0,
            prompt="Choose any number of Fire Energy to discard")
        if discarded:
            await ctx.discard_cards(list(discarded))
    await ctx.deal_damage(10 + 10 * len(discarded))


card = PokemonCardDef(
    guid="da1bf7db-3f6b-5328-9e2b-536f3efb13b1",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    display_name="Magmar",
    searchable_by=["Magmar", "Basic", "Magmar"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=126,
    abilities=[
        Attack(
            title="Burning Fire",
            game_text="When you use this attack, you may discard any number of Fire Energy cards attached to your Pok\u00e9mon in play. This attack does 10 damage plus 10 more damage for each Fire Energy card you discarded in this way.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="+",
            effect=burning_fire,
        ),
        Attack(
            title="Magma Punch",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)