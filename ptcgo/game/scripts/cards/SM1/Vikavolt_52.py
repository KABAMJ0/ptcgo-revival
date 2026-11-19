from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.content.definitions import Activations
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import distribute_energy


def _energy_of(type_value):
    return lambda card: energy_provides_type(card, type_value)


async def _strong_charge(ctx):
    picked = await ctx.search_deck_groups([
        (_energy_of(PokemonTypes.GRASS.value), 1, "a Grass Energy card"),
        (_energy_of(PokemonTypes.LIGHTNING.value), 1, "a Lightning Energy card"),
    ], prompt="Choose a Grass Energy and a Lightning Energy to attach")
    cards = [card for group in picked for card in group]
    await ctx.shuffle_deck()
    if not cards:
        return
    candidates = ctx.my_pokemon_in_play()
    if candidates:
        await distribute_energy(ctx, cards, candidates)


card = PokemonCardDef(
    guid="94b9d9b7-5ccf-5cf9-bf94-4df54aa59e5d",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vikavolt.Name",
    display_name="Vikavolt",
    searchable_by=["Vikavolt", "Stage 2", "Vikavolt"],
    subtypes=["Stage 2"],
    collector_number=52,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    family_id=736,
    abilities=[
        Ability(
            title="Strong Charge",
            game_text="Once during your turn (before your attack), you may search your deck for a Grass Energy card and a Lightning Energy card and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            effect=_strong_charge,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Electro Cannon",
            game_text="Discard 3 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=self_energy_discard_attack(count=3),
        ),
    ],
)