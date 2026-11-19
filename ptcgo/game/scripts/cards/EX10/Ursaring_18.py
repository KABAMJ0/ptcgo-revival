from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_bonus

card = PokemonCardDef(
    guid="3f588ac1-d1ba-5a34-8990-46ce1536b1ed",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name",
    display_name="Ursaring",
    searchable_by=["Ursaring", "Stage 1", "Ursaring"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    family_id=216,
    abilities=[
        Ability(
            title="Intimidating Ring",
            game_text="As long as Ursaring is your Active Pok\u00e9mon, your opponent's Basic Pok\u00e9mon can't attack or use any Pok\u00e9-Powers.",
            effect=unimplemented,
        ),
        Attack(
            title="Drag Off",
            game_text="Before doing damage, you may switch 1 of your opponent's Benched Pok\u00e9mon with the Defending Pok\u00e9mon. If you do, this attack does 20 damage to the new Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Rock Smash",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)