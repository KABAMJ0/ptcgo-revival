from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID

async def form_change(ctx):
    source = ctx.source
    if source is None:
        return
    want = source.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    pool = [card for card in ctx.deck()
            if card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == want]
    if not pool:
        return
    picked = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose another Deoxys from your deck")
    if not picked:
        return
    await ctx.identity_swap(source, picked[0], destination="deck")
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="4a008dfa-84d4-5924-a621-7f45225fa16d",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="EX8",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Ability(
            title="Form Change",
            game_text="Once during your turn (before your attack), you may search your deck for another Deoxys and switch it with Deoxys. (Any cards attached to Deoxys, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) If you do, put Deoxys on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Pok\u00e9-Power each turn.",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Form Change",
            effect=form_change,
        ),
        Attack(
            title="Energy Crush",
            game_text="Does 10 damage plus 10 more damage for each Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)