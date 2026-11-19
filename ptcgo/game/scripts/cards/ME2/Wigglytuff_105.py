from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_with_attack, damage_per

card = PokemonCardDef(
    guid="8b2f941e-1636-5361-8878-cc01c029324d",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuff.Name",
    display_name="Wigglytuff",
    searchable_by=["Wigglytuff", "Stage 1", "Wigglytuff"],
    subtypes=["Stage 1"],
    collector_number=105,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Attack(
            title="Round",
            game_text="This attack does 40 damage for each of your Pok\u00e9mon in play that has the Round attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            effect=damage_per(count_with_attack("Round"), 40),
        ),
        Attack(
            title="Seismic Toss",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)