from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="17cd7759-0e0f-5e91-8378-277eb5c49bf4",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatitoex.Name",
    display_name="Sprigatito ex",
    searchable_by=["Sprigatito ex", "Basic", "ex", "Sprigatitoex"],
    subtypes=["Basic", "ex"],
    collector_number=251,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=906,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Magical Leaf",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=heal_attack(30),
        ),
    ],
)