from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5d8259e2-c9c4-5369-bac7-e6c8e74fa3b6",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1", "Raichu"],
    subtypes=["Stage 1"],
    collector_number=132,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Ability(
            title="Electrical Grounding",
            game_text="When 1 of your Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, you may move a Lightning Energy from that Pok\u00e9mon to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Thunder",
            game_text="This Pok\u00e9mon also does 50 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=recoil_attack(50),
        ),
    ],
)