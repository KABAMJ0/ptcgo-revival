from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import heal_dealt_attack
from ptcgo.game.card_effects.attacks_common import damage_reduction_on_self


card = PokemonCardDef(
    guid="d4801e6b-f32d-5cfa-9670-82412ba13628",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palossand.Name",
    display_name="Palossand",
    searchable_by=["Palossand", "Stage 1", "Palossand"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="SM1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    family_id=769,
    abilities=[
        Ability(
            title="Wall of Sand",
            game_text="This Pok\u00e9mon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            effect=damage_reduction_on_self(per=20),
        ),
        Attack(
            title="Absorb Vitality",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=heal_dealt_attack(),
        ),
    ],
)