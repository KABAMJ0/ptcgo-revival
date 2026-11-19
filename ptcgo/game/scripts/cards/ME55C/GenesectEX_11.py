from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="b8e9e0d8-4907-5cf8-87d6-6007400ba923",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GenesectEX.Name",
    display_name="Genesect-EX",
    searchable_by=["Genesect-EX", "Basic", "EX", "GenesectEX"],
    subtypes=["Basic", "EX"],
    collector_number=11,
    set_code="ME55C",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=649,
    abilities=[
        Ability(
            title="Red Signal",
            game_text="When you attach a Plasma Energy from your hand to this Pok\u00e9mon, you may switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Megalo Cannon",
            game_text="Does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=snipe_attack(20, pool="bench", apply_modifiers=False),
        ),
    ],
)