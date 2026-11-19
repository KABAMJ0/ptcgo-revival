from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.content.definitions import Activations
from ptcgo.game.card_effects.attacks_common import place_counters
from ptcgo.game.card_effects.pokemon import is_fire_energy
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8cae49b3-008d-557a-a23f-28662866bc00",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=158,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=6,
    abilities=[
        Ability(
            title="Roaring Resolve",
            game_text="Once during your turn (before your attack), you may put 2 damage counters on this Pok\u00e9mon. If you do, search your deck for up to 2 Fire Energy cards and attach them to this Pok\u00e9mon. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=place_counters(2, target="self", also=search_attach_energy(
                predicate=is_fire_energy, count=2, to_self=True)),
        ),
        Attack(
            title="Continuous Blaze Ball",
            game_text="Discard all Fire Energy from this Pok\u00e9mon. This attack does 50 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)