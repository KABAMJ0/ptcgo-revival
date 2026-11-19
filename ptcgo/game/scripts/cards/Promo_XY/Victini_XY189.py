from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

async def energy_assist(ctx):
    """Flip a coin; on heads attach a basic Energy from the discard pile to a
    Benched Pokemon."""
    if not (await ctx.flip_coins(1, "Energy Assist"))[0]:
        return
    from ptcgo.game.card_effects.pokemon import is_energy_card
    from ptcgo.game.attributes import AttrID as _AttrID
    discard = ctx.discard_pile(ctx.player_id)
    energies = [c for c in discard if is_energy_card(c)
                and not bool(c.get_attribute(_AttrID.IS_SPECIAL_ENERGY))]
    bench = ctx.my_bench()
    if not energies or not bench:
        return
    card = (await ctx.choose_cards(energies, 1, prompt="Choose a basic Energy from your discard pile"))[0]
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokemon to attach it to")
    if card is not None and target is not None:
        await ctx.attach_energy(card, target)


card = PokemonCardDef(
    guid="b43b69f9-2232-517f-8ce8-1fb2d429ea58",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic", "Victini"],
    subtypes=["Basic"],
    collector_number=189,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="Energy Assist",
            game_text="Flip a coin. If heads, attach a basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=energy_assist,
        ),
        Attack(
            title="Victory Ball",
            game_text="Discard a Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.FIRE),
        ),
    ],
)