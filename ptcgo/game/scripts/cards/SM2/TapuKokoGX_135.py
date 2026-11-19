from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import is_lightning_energy


async def aero_trail(ctx):
    """On play from hand to the Bench: you may move any number of Lightning
    Energy from your other Pokemon to this Pokemon, then switch it in."""
    me = ctx.source
    others = [p for p in ctx.my_pokemon_in_play() if p is not me]
    if not any(is_lightning_energy(energy)
               for pokemon in others
               for energy in ctx.attached_energies(pokemon)):
        return
    if not await ctx.ask_yes_no(
        "Move any number of Lightning Energy from your other Pok\u00e9mon "
        "to this Pok\u00e9mon?"
    ):
        return
    moved = await ctx.move_energy_freely(
        others, [me], predicate=is_lightning_energy,
        prompt="Choose Lightning Energy to move")
    if moved and me is not ctx.my_active():
        await ctx.switch_active(ctx.player_id, me)


card = PokemonCardDef(
    guid="2357cd14-5b6b-5ea8-a414-43c0835a432f",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoGX.Name",
    display_name="Tapu Koko-GX",
    searchable_by=["Tapu Koko-GX", "Basic", "GX", "TapuKokoGX"],
    subtypes=["Basic", "GX"],
    collector_number=135,
    set_code="SM2",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=785,
    abilities=[
        Ability(
            title="Aero Trail",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may move any number of Lightning Energy from your other Pok\u00e9mon to this Pok\u00e9mon. If you do, switch this Pok\u00e9mon with your Active Pok\u00e9mon.",
            trigger=Triggers.ON_PLAY,
            effect=aero_trail,
        ),
        Attack(
            title="Sky-High Claws",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title="Tapu Thunder-GX",
            game_text="This attack does 50 damage times the amount of Energy attached to all of your opponent's Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_energy("opponent"), 50),
        ),
    ],
)