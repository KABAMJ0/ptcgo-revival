from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import takes_less_passive
from ptcgo.game.card_effects.attacks_common import spread_damage

card = PokemonCardDef(
    guid="6715b771-16e6-522f-b53b-b93cdcda23c2",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Copperajahex.Name",
    display_name="Copperajah ex",
    searchable_by=["Copperajah ex", "Stage 1", "ex", "Copperajahex"],
    subtypes=["Stage 1", "ex"],
    collector_number=150,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=300,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name",
    family_id=878,
    abilities=[
        Ability(
            title="Bronze Body",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Nosequake",
            game_text="This attack also does 30 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=260,
            effect=spread_damage(30, side="mine"),
        ),
    ],
)