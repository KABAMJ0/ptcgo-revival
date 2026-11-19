from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench


async def _move_energy_to_new_bench(ctx, benched):
    attached = ctx.attached_energies(ctx.attacker)
    if not attached or not benched:
        return
    picks = attached if len(attached) == 1 else await ctx.choose_cards(
        attached, 1, prompt="Choose an Energy to move to the new Benched Pok\u00e9mon")
    if not picks:
        return
    target = benched[0] if len(benched) == 1 else await ctx.choose_pokemon(
        benched, "Choose a Benched Pok\u00e9mon to move the Energy to")
    if target is not None:
        await ctx.move_energy(picks[0], target)


card = PokemonCardDef(
    guid="67f67e1d-ddec-5c78-8093-cd3604395d4d",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic", "Jynx"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=124,
    abilities=[
        Attack(
            title="Inviting Kiss",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Then, shuffle your deck. If you put any Pok\u00e9mon onto your Bench in this way, move an Energy from this Pok\u00e9mon to the new Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(then=_move_energy_to_new_bench),
        ),
        Attack(
            title="Icy Snow",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
    ],
)