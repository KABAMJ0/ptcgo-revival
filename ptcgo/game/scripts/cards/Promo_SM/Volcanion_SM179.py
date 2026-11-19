from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, count_energy
from ptcgo.game.card_effects.support_common import search_attach_energy

async def flare_starter(ctx):
    """Search the deck for a Fire Energy and attach it; going second on the
    first turn, instead search up to 3 and attach them in any way you like."""
    from ptcgo.game.card_effects.pokemon import is_basic_fire_energy
    going_second_first_turn = (
        getattr(ctx.session, "first_player_id", None) not in (None, ctx.player_id)
        and ctx.session.turn_state.turn_number <= 2)
    count = 3 if going_second_first_turn else 1
    await search_attach_energy(is_basic_fire_energy, count, to_self=False,
                               distribute=True,
                               prompt="Choose Fire Energy to attach")(ctx)


card = PokemonCardDef(
    guid="ecd53342-890c-5fca-9d11-a0ec65c47e3e",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name",
    display_name="Volcanion",
    searchable_by=["Volcanion", "Basic", "Volcanion"],
    subtypes=["Basic"],
    collector_number=179,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Attack(
            title="Flare Starter",
            game_text="Search your deck for a Fire Energy card and attach it to 1 of your Pok\u00e9mon. If you go second and it's your first turn, instead search for up to 3 Fire Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=flare_starter,
        ),
        Attack(
            title="High-Heat Blast",
            game_text="If you have at least 4 Fire Energy in play, this attack does 60 more damage.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(lambda ctx: count_energy("mine", PokemonTypes.FIRE)(ctx) >= 4, 60),
        ),
    ],
)