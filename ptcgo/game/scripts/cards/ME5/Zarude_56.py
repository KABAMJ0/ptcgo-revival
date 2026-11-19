from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="0e7caebe-07a0-500f-af33-1f52a7070f7d",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zarude.Name",
    display_name="Zarude",
    searchable_by=["Zarude", "Basic", "Zarude"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=893,
    abilities=[
        Attack(
            title="Overhead Throw",
            game_text="This attack also does 30 damage to 1 of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=snipe_attack(30, pool='bench', side='mine', also_base=True),
        ),
        Attack(
            title="Shadowy Whip",
            game_text="If your Benched Pok\u00e9mon have any Shadowy Darkness Energy attached, this attack does 70 more damage.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)