from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="e6b4a56f-3b6d-5226-a429-5103760b5a68",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1", "Raichu"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="SM3",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Ability(
            title="Evoshock",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may leave your opponent's Active Pok\u00e9mon Paralyzed.",
            effect=unimplemented,
        ),
        Attack(
            title="Volt Tackle",
            game_text="This Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=recoil_attack(30),
        ),
    ],
)