from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _water_cyclone_ready(board, player_id, pokemon) -> bool:
    return unafflicted(board, player_id, pokemon) and bool(
        board.active_pokemon(player_id) is not None
        and any(energy_provides_type(e, PokemonTypes.WATER.value)
                for e in board.attached_energies(board.active_pokemon(player_id))))


async def _water_cyclone(ctx):
    active = ctx.my_active()
    bench = ctx.my_bench()
    if active is None or not bench:
        return
    water = [e for e in ctx.attached_energies(active)
             if energy_provides_type(e, PokemonTypes.WATER.value)]
    if not water:
        return
    picks = await ctx.choose_cards(
        water, 1, prompt="Choose a Water Energy to move from your Active Pok\u00e9mon")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pok\u00e9mon to attach the Energy to")
    if target is not None:
        await ctx.move_energy(picks[0], target)

card = PokemonCardDef(
    guid="93772025-6a68-54a6-8931-3d035ed84599",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Ability(
            title="Water Cyclone",
            game_text="As often as you like during your turn (before your attack), you may move a Water Energy card from your Active Pok\u00e9mon to 1 of your Benched Pok\u00e9mon. This power can't be used if Kingdra is affected by a Special Condition.",
            activation=Activations.UNLIMITED,
            condition=_water_cyclone_ready,
            effect=_water_cyclone,
        ),
        Attack(
            title="Rapids",
            game_text="Flip a coin. If heads, discard 1 Energy card attached to the Defending Pok\u00e9mon, if any.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=discard_opponent_energy_attack(count=1, flip=True),
        ),
    ],
)
