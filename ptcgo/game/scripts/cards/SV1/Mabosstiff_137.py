from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8619ac4c-20a1-5c1d-8ab0-ae88e1bf5133",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mabosstiff.Name",
    display_name="Mabosstiff",
    searchable_by=["Mabosstiff", "Stage 1", "Mabosstiff"],
    subtypes=["Stage 1"],
    collector_number=137,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name",
    family_id=942,
    abilities=[
        Ability(
            title="Intimidating Howl",
            game_text="Once during your turn, you may switch out your opponent's Active Pok\u00e9mon to the Bench.\u00a0(Your opponent chooses the new Active Pok\u00e9mon.)",
            effect=unimplemented,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=recoil_attack(30),
        ),
    ],
)