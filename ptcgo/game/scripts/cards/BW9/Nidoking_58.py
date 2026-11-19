from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_bench, damage_per

card = PokemonCardDef(
    guid="32070912-a6b7-5962-b225-d10897c0f58b",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking",
    searchable_by=["Nidoking", "Stage 2", "Nidoking"],
    subtypes=["Stage 2"],
    collector_number=58,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    family_id=32,
    abilities=[
        Attack(
            title="Lovestrike",
            game_text="Does 40 more damage for each Nidoqueen on your Bench.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_bench("mine", lambda p: p.get_attribute(
                AttrID.EVOLUTION_LOGIC_NAME) == "Nidoqueen"), 40, base=20),
        ),
        Attack(
            title="Horn Drill",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)