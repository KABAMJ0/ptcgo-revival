from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1a92bbda-9743-503c-82a3-36479973a256",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronThorns.Name",
    display_name="Iron Thorns",
    searchable_by=["Iron Thorns", "Basic", "Future", "IronThorns"],
    subtypes=["Basic", "Future"],
    collector_number=98,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=995,
    abilities=[
        Attack(
            title="Destructo-Press",
            game_text="Reveal the top 5 cards of your deck. This attack does 70 damage for each Future card you find there. Then, discard those Future cards and shuffle the other cards back into your deck.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Megaton Lariat",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)