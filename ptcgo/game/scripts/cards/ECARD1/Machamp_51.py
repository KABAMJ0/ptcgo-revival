from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.attacks_common import damage_per, flip_gate

async def effect(ctx):
    await ctx.reorder_deck_top(4)


def _damaged_in_play(ctx):
    return sum(1 for p in ctx.my_pokemon_in_play()
               if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p))


card = PokemonCardDef(
    guid="2fb0d475-2251-5b5a-858c-b2371dc8b4ba",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=51,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Terraforming",
            game_text="Once during your turn (before your attack), you may look at the top 4 cards of your deck and rearrange them as you like. This power can't be used if Machamp is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=lambda board, player_id, pokemon: not pokemon.get_attribute(
                AttrID.SPECIAL_CONDITIONS),
            effect=effect,
        ),
        Attack(
            title="Iron Fist",
            game_text="Count the number of Pok\u00e9mon you have in play with damage counters on them. Flip a coin. If heads, this attack does 50 damage plus 10 more damage for each of those Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_gate(then=damage_per(_damaged_in_play, 10, base=50)),
        ),
    ],
)