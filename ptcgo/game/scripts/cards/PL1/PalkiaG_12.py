from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import spread_damage

card = PokemonCardDef(
    guid="2524a098-dbcb-520b-b2d7-a309f0a425fc",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PalkiaG.Name",
    display_name="Palkia G",
    searchable_by=["Palkia G", "Basic", "SP", "PalkiaG"],
    subtypes=["Basic", "SP"],
    collector_number=12,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=484,
    abilities=[
        Attack(
            title="Splashing Turn",
            game_text="You may switch Palkia G with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Pearl Breath",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=spread_damage(10, side="opponent", include_active=False),
        ),
    ],
)