from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.trainers import is_basic_energy_card


async def _reflect_energy(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    basics = [energy for energy in ctx.attached_energies(ctx.attacker)
              if is_basic_energy_card(energy)]
    if not bench or not basics:
        return
    energy = basics[0]
    if len(basics) > 1:
        picked = await ctx.choose_cards(
            basics, 1, prompt="Choose a basic Energy card to move to your Bench")
        if not picked:
            return
        energy = picked[0]
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to attach the Energy to")
    if target is not None:
        await ctx.move_energy(energy, target)


card = PokemonCardDef(
    guid="20a99c22-ec1c-5a3c-b265-977a6650d9c6",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    display_name="Electabuzz",
    searchable_by=["Electabuzz", "Basic", "Electabuzz"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=125,
    abilities=[
        Attack(
            title="Energy Draw",
            game_text="Search your deck for a basic Energy card and attach it to Electabuzz. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_attach_energy(predicate=is_basic_energy_card, count=1, to_self=True),
        ),
        Attack(
            title="Reflect Energy",
            game_text="If you have any Benched Pok\u00e9mon and if there are any basic Energy cards attached to Electabuzz, take 1 of those Energy cards and attach it to 1 of those Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_reflect_energy,
        ),
    ],
)