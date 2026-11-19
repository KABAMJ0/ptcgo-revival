from ptcgo.game.card_effects.attacks_common import damage_per, count_bench
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="333e6341-6ab9-5a9c-b22d-f4625d7a00c8",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name",
    display_name="Nidoqueen",
    searchable_by=["Nidoqueen", "Stage 2", "Nidoqueen"],
    subtypes=["Stage 2"],
    collector_number=30,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    family_id=29,
    abilities=[
        Ability(
            title="Maternal Comfort",
            game_text="At any times between turns, remove 1 damage counter from each of your Pok\u00e9mon. You can't use more than 1 Maternal Comfort Pok\u00e9-Body between turns.",
            effect=unimplemented,
        ),
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
        ),
        Attack(
            title="Ruthless Tail",
            game_text="Does 50 damage plus 10 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_bench("opponent"), 10, base=50),
        ),
    ],
)