from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import switch_self_attack
from ptcgo.game.card_effects.passives_common import previous_evolution_grant_passive


card = PokemonCardDef(
    guid="38302287-4728-529d-92e8-6ef454d17735",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CelebiEX.Name",
    display_name="Celebi-EX",
    searchable_by=["Celebi-EX", "Basic", "EX", "CelebiEX"],
    subtypes=["Basic", "EX"],
    collector_number=9,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=251,
    abilities=[
        Ability(
            title="Time Recall",
            game_text="Each of your evolved Pok\u00e9mon can use any attack from its previous Evolutions. (You still need the necessary Energy to use each attack.)",
            passive=previous_evolution_grant_passive(),
        ),
        Attack(
            title="Wind Whisk",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=switch_self_attack(),
        ),
    ],
)