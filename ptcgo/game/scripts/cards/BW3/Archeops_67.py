from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import evolution_lock_passive

card = PokemonCardDef(
    guid="c46546cf-1e8c-52e8-a10d-53b49941a0ec",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archeops.Name",
    display_name="Archeops",
    searchable_by=["Archeops", "Stage 1", "Archeops"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Archen.Name",
    family_id=566,
    abilities=[
        Ability(
            title="Ancient Power",
            game_text="Each play can't play any Pok\u00e9mon from his or her hand to evolve his or her Pok\u00e9mon.",
            passive=evolution_lock_passive(),
        ),
        Attack(
            title="Rock Slide",
            game_text="Does 10 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)