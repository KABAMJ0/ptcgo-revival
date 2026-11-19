from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.support_common import search_attach_energy

async def strong_charge(ctx):
    """Search the deck for a Grass Energy and a Lightning Energy and attach
    both, in any way you like."""
    from ptcgo.game.card_effects.pokemon import energy_provides_type
    for type_value in (PokemonTypes.GRASS.value, PokemonTypes.LIGHTNING.value):
        await search_attach_energy(
            lambda c, t=type_value: energy_provides_type(c, t), 1, to_self=False,
            distribute=True, prompt="Choose an Energy to attach")(ctx)


card = PokemonCardDef(
    guid="5a427e0f-e3b5-5b44-8e93-262725c24d27",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vikavolt.Name",
    display_name="Vikavolt",
    searchable_by=["Vikavolt", "Stage 2", "Vikavolt"],
    subtypes=["Stage 2"],
    collector_number=28,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    family_id=738,
    abilities=[
        Ability(
            title="Strong Charge",
            game_text="Once during your turn (before your attack), you may search your deck for a Grass Energy card and a Lightning Energy card and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=strong_charge,
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