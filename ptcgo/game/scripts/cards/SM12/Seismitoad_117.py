from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.trainers import search_to_top
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.attacks_common import damage_per


def _damaged_bench(ctx) -> int:
    return sum(1 for pokemon in ctx.my_bench()
               if (pokemon.get_attribute(AttrID.HP) or 0) < ctx.max_hp(pokemon))

card = PokemonCardDef(
    guid="efcf3d74-4c16-5430-8be9-b5bd24a30fcc",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name",
    display_name="Seismitoad",
    searchable_by=["Seismitoad", "Stage 2", "Seismitoad"],
    subtypes=["Stage 2"],
    collector_number=117,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    family_id=535,
    abilities=[
        Ability(
            title="Bulldoze",
            game_text="Once during your turn (before your attack), you may search your deck for a card, shuffle your deck, then put that card on top of it.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_to_top(1),
        ),
        Attack(
            title="Tremulous Fist",
            game_text="This attack does 30 more damage for each of your Benched Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=damage_per(_damaged_bench, 30, base=80),
        ),
    ],
)