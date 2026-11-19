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
    guid="3202f893-59ca-55f2-ae0b-971cb0962c04",
    key="POP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys δ",
    searchable_by=["Deoxys \u03b4", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="POP4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
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
            title="Crystal Laser",
            game_text="During your next turn, Deoxys's attacks do 40 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=unimplemented,
        ),
    ],
)