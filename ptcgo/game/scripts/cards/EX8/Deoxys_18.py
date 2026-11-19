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
    guid="7a46252f-aa00-5db5-bb50-b6e039122751",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=18,
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
            title="Barrier Attack",
            game_text="During your opponent's next turn, any damage done to Deoxys by attacks is reduced by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)