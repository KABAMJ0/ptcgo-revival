from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.session.passives import is_basic_energy
from ptcgo.game.content.definitions import def_for


def _basic_darkness_energy(card):
    return is_basic_energy(card) and energy_provides_type(
        card, PokemonTypes.DARKNESS.value)


async def _coordinated_pack(ctx):
    pack = [pokemon for pokemon in ctx.my_bench()
            if "houndour" in (def_for(pokemon.archetype_id).display_name or "").lower()]
    energies = [card for card in ctx.deck() if _basic_darkness_energy(card)]
    for pokemon in pack:
        if not energies:
            break
        picks = await ctx.choose_cards(
            energies, 1, minimum=0,
            prompt="Choose a Basic Darkness Energy to attach to Houndour")
        if not picks:
            break
        energies.remove(picks[0])
        await ctx.attach_energy(picks[0], pokemon)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="fd973ae3-477c-555a-96c5-136f8b353988",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    display_name="Houndour",
    searchable_by=["Houndour", "Basic", "Houndour"],
    subtypes=["Basic"],
    collector_number=204,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=228,
    abilities=[
        Attack(
            title="Coordinated Pack",
            game_text="For each of your Benched Houndour, search your deck for a Basic Darkness Energy card and attach it to that Houndour. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=_coordinated_pack,
        ),
        Attack(
            title="Focus Fangs",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)